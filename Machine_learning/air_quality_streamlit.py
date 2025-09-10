import streamlit as st
import pickle
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

# Page configuration
st.set_page_config(
    page_title="AQI Prediction Dashboard",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
    }
    
    .sub-header {
        font-size: 1.5rem;
        color: #333;
        margin-bottom: 1rem;
    }
    
    .metric-container {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #1f77b4;
    }
    
    .aqi-good { background: linear-gradient(90deg, #00e400 0%, #ffff00 100%); }
    .aqi-moderate { background: linear-gradient(90deg, #ffff00 0%, #ff7e00 100%); }
    .aqi-unhealthy-sensitive { background: linear-gradient(90deg, #ff7e00 0%, #ff0000 100%); }
    .aqi-unhealthy { background: linear-gradient(90deg, #ff0000 0%, #8f3f97 100%); }
    .aqi-very-unhealthy { background: linear-gradient(90deg, #8f3f97 0%, #7e0023 100%); }
    .aqi-hazardous { background: #7e0023; }
</style>
""", unsafe_allow_html=True)

# Helper functions
def get_aqi_category(aqi_value):
    """Return AQI category and color based on value"""
    if aqi_value <= 50:
        return "Good", "#00e400"
    elif aqi_value <= 100:
        return "Moderate", "#ffff00"
    elif aqi_value <= 150:
        return "Unhealthy for Sensitive Groups", "#ff7e00"
    elif aqi_value <= 200:
        return "Unhealthy", "#ff0000"
    elif aqi_value <= 300:
        return "Very Unhealthy", "#8f3f97"
    else:
        return "Hazardous", "#7e0023"

def get_aqi_description(aqi_value):
    """Return health implications based on AQI value"""
    if aqi_value <= 50:
        return "Air quality is satisfactory, and air pollution poses little or no risk."
    elif aqi_value <= 100:
        return "Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
    elif aqi_value <= 150:
        return "Members of sensitive groups may experience health effects. The general public is less likely to be affected."
    elif aqi_value <= 200:
        return "Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
    elif aqi_value <= 300:
        return "Health alert: The risk of health effects is increased for everyone."
    else:
        return "Health warning of emergency conditions: everyone is more likely to be affected."

def load_model():
    """Load the trained Random Forest model"""
    try:
        with open('air_quality.pkl', 'rb') as file:
            model = pickle.load(file)
        return model, True
    except FileNotFoundError:
        return None, False

def create_gauge_chart(aqi_value, title="Overall AQI"):
    """Create a gauge chart for AQI visualization"""
    fig = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        value = aqi_value,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': title, 'font': {'size': 24}},
        gauge = {
            'axis': {'range': [None, 500], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "darkblue"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 50], 'color': '#00e400'},
                {'range': [50, 100], 'color': '#ffff00'},
                {'range': [100, 150], 'color': '#ff7e00'},
                {'range': [150, 200], 'color': '#ff0000'},
                {'range': [200, 300], 'color': '#8f3f97'},
                {'range': [300, 500], 'color': '#7e0023'}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': aqi_value
            }
        }
    ))
    
    fig.update_layout(height=400, font={'color': "darkblue", 'family': "Arial"})
    return fig

def create_component_chart(co_aqi, ozone_aqi, no2_aqi, pm25_aqi):
    """Create bar chart for AQI components"""
    components = ['CO AQI', 'Ozone AQI', 'NO2 AQI', 'PM2.5 AQI']
    values = [co_aqi, ozone_aqi, no2_aqi, pm25_aqi]
    colors = ['#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
    
    fig = go.Figure(data=[
        go.Bar(x=components, y=values, marker_color=colors, text=values, textposition='auto')
    ])
    
    fig.update_layout(
        title="AQI Components Breakdown",
        xaxis_title="Components",
        yaxis_title="AQI Value",
        height=400,
        showlegend=False
    )
    
    return fig

# Main app
def main():
    # Header
    st.markdown('<h1 class="main-header">🌍 Air Quality Index Prediction Dashboard</h1>', unsafe_allow_html=True)
    
    # Load model
    model, model_loaded = load_model()
    
    if not model_loaded:
        st.error("⚠️ Model file 'aqi_model.pkl' not found. Please ensure the trained model is in the same directory.")
        st.info("📋 Expected model input features: ['co aqi value', 'ozone aqi value', 'no2 aqi value', 'pm2.5 aqi value']")
        return
    
    # Sidebar for inputs
    st.sidebar.markdown("## 🎛️ Input Parameters")
    st.sidebar.markdown("Enter the AQI values for different pollutants:")
    
    # Input fields
    co_aqi = st.sidebar.number_input(
        "CO AQI Value",
        min_value=0,
        max_value=500,
        value=1,
        help="Carbon Monoxide AQI Value (0-500)"
    )
    
    ozone_aqi = st.sidebar.number_input(
        "Ozone AQI Value",
        min_value=0,
        max_value=500,
        value=36,
        help="Ground-level Ozone AQI Value (0-500)"
    )
    
    no2_aqi = st.sidebar.number_input(
        "NO2 AQI Value",
        min_value=0,
        max_value=500,
        value=0,
        help="Nitrogen Dioxide AQI Value (0-500)"
    )
    
    pm25_aqi = st.sidebar.number_input(
        "PM2.5 AQI Value",
        min_value=0,
        max_value=500,
        value=51,
        help="Fine Particulate Matter AQI Value (0-500)"
    )
    
    # Prediction button
    predict_button = st.sidebar.button("🔮 Predict AQI", type="primary")
    
    # Main content area
    if predict_button or 'predicted_aqi' not in st.session_state:
        # Prepare input data
        input_data = pd.DataFrame({
            'co aqi value': [co_aqi],
            'ozone aqi value': [ozone_aqi],
            'no2 aqi value': [no2_aqi],
            'pm2.5 aqi value': [pm25_aqi]
        })
        
        # Make prediction
        try:
            predicted_aqi = model.predict(input_data)[0]
            st.session_state.predicted_aqi = predicted_aqi
            st.session_state.input_values = [co_aqi, ozone_aqi, no2_aqi, pm25_aqi]
        except Exception as e:
            st.error(f"Error making prediction: {str(e)}")
            return
    
    if 'predicted_aqi' in st.session_state:
        predicted_aqi = st.session_state.predicted_aqi
        category, color = get_aqi_category(predicted_aqi)
        description = get_aqi_description(predicted_aqi)
        
        # Results section
        col1, col2 = st.columns([1, 1])
        
        with col1:
            # Gauge chart
            gauge_fig = create_gauge_chart(predicted_aqi)
            st.plotly_chart(gauge_fig, use_container_width=True)
            
            # AQI Information
            st.markdown(f"""
            <div class="metric-container">
                <h3>🎯 Predicted AQI: <span style="color: {color};">{predicted_aqi:.1f}</span></h3>
                <h4>Category: <span style="color: {color};">{category}</span></h4>
                <p><strong>Health Implications:</strong></p>
                <p>{description}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            # Component breakdown chart
            component_fig = create_component_chart(co_aqi, ozone_aqi, no2_aqi, pm25_aqi)
            st.plotly_chart(component_fig, use_container_width=True)
            
            # Component details
            st.markdown("### 📊 Input Component Details")
            components_df = pd.DataFrame({
                'Component': ['CO AQI', 'Ozone AQI', 'NO2 AQI', 'PM2.5 AQI'],
                'Value': [co_aqi, ozone_aqi, no2_aqi, pm25_aqi],
                'Category': [get_aqi_category(val)[0] for val in [co_aqi, ozone_aqi, no2_aqi, pm25_aqi]]
            })
            st.dataframe(components_df, use_container_width=True)
        
        # Historical comparison (mock data for demonstration)
        st.markdown("---")
        st.markdown("### 📈 Trend Analysis")
        
        # Create sample trend data
        dates = pd.date_range(start='2024-01-01', periods=30, freq='D')
        np.random.seed(42)
        trend_data = pd.DataFrame({
            'Date': dates,
            'Predicted_AQI': np.random.normal(predicted_aqi, 15, 30).clip(0, 500)
        })
        
        trend_fig = px.line(trend_data, x='Date', y='Predicted_AQI', 
                           title='30-Day AQI Trend (Simulated)',
                           line_shape='spline')
        trend_fig.add_hline(y=predicted_aqi, line_dash="dash", line_color="red",
                           annotation_text=f"Current Prediction: {predicted_aqi:.1f}")
        
        # Add AQI category zones
        trend_fig.add_hrect(y0=0, y1=50, fillcolor="green", opacity=0.1, annotation_text="Good")
        trend_fig.add_hrect(y0=50, y1=100, fillcolor="yellow", opacity=0.1, annotation_text="Moderate")
        trend_fig.add_hrect(y0=100, y1=150, fillcolor="orange", opacity=0.1, annotation_text="Unhealthy for Sensitive")
        
        st.plotly_chart(trend_fig, use_container_width=True)
        
        # Additional insights
        st.markdown("---")
        st.markdown("### 💡 Insights & Recommendations")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            dominant_pollutant = ['CO', 'Ozone', 'NO2', 'PM2.5'][np.argmax([co_aqi, ozone_aqi, no2_aqi, pm25_aqi])]
            st.info(f"🔍 **Dominant Pollutant:** {dominant_pollutant}")
        
        with col2:
            avg_component = np.mean([co_aqi, ozone_aqi, no2_aqi, pm25_aqi])
            if predicted_aqi > avg_component:
                st.warning("⚠️ **Synergistic Effect:** Combined pollutants create higher AQI")
            else:
                st.success("✅ **Additive Effect:** AQI reflects individual components")
        
        with col3:
            if predicted_aqi > 100:
                st.error("🏠 **Recommendation:** Limit outdoor activities")
            else:
                st.success("🌟 **Recommendation:** Safe for outdoor activities")
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; font-size: 0.8rem;">
        <p>🤖 Powered by Random Forest Regression | Built with Streamlit</p>
        <p>⚠️ This is a predictive model. For official AQI readings, consult local environmental agencies.</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()