import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Black and White Intensity Image Generator")
st.write("Upload a numpy array (matrix) to generate a black and white intensity image")

# Option 1: Manual input for array
default_matrix = np.array([[202, 145,  31,  72, 124],
                          [ 63,  82, 262,  34,  40],
                          [ 81,  91,  98, 263,  78],
                          [ 39, 109,   4, 208,  15],
                          [ 27, 293, 209,  11, 298]])

st.subheader("Method 1: Editable Matrix")
matrix_str = st.text_area("Enter your matrix (comma-separated values, rows separated by new lines):", 
                         value="202,145,31,72,124\n63,82,262,34,40\n81,91,98,263,78\n39,109,4,208,15\n27,293,209,11,298",
                         height=150)

# Option 2: File upload
st.subheader("Method 2: Upload .npy file")
uploaded_file = st.file_uploader("Choose a .npy file", type="npy")

# Process the input
def parse_matrix(matrix_str):
    try:
        rows = matrix_str.strip().split('\n')
        matrix = []
        for row in rows:
            if row.strip():
                values = [int(x.strip()) for x in row.split(',')]
                matrix.append(values)
        return np.array(matrix)
    except Exception as e:
        st.error(f"Error parsing matrix: {e}")
        return None

def validate_and_normalize_matrix(matrix):
    if matrix is None:
        return False, None
    if matrix.size == 0:
        st.error("Matrix is empty")
        return False, None
    
    # Automatically scale values to 0-255 range
    min_val = matrix.min()
    max_val = matrix.max()
    
    if min_val < 0 or max_val > 255:
        st.warning(f"Matrix values range from {min_val} to {max_val}. Automatically scaling to 0-255 range.")
        if min_val < 0:
            matrix = matrix - min_val  # Shift to make min 0
            max_val = matrix.max()
        if max_val > 0:  # Avoid division by zero
            matrix = (matrix * 255.0 / max_val).astype(np.uint8)
    
    return True, matrix

def display_image(matrix):
    fig, ax = plt.subplots(figsize=(10, 8))
    # Use the actual min/max values for display range
    im = ax.imshow(matrix, cmap='gray', vmin=matrix.min(), vmax=matrix.max())
    ax.set_title("Black and White Intensity Image")
    plt.colorbar(im, ax=ax, label="Intensity Value")
    st.pyplot(fig)
    
    # Display matrix info
    st.write(f"Matrix shape: {matrix.shape}")
    st.write(f"Min value: {matrix.min()}")
    st.write(f"Max value: {matrix.max()}")

# Process manual input
if matrix_str:
    matrix = parse_matrix(matrix_str)
    is_valid, normalized_matrix = validate_and_normalize_matrix(matrix)
    if is_valid:
        st.subheader("Generated Image (Manual Input)")
        display_image(normalized_matrix)

# Process uploaded file
if uploaded_file is not None:
    try:
        matrix = np.load(uploaded_file)
        is_valid, normalized_matrix = validate_and_normalize_matrix(matrix)
        if is_valid:
            st.subheader("Generated Image (Uploaded File)")
            display_image(normalized_matrix)
    except Exception as e:
        st.error(f"Error loading file: {e}")

st.markdown("""
### Instructions:
1. **Method 1**: Edit the matrix in the text area above. 
   - Enter comma-separated values for each row
   - Separate rows with new lines
2. **Method 2**: Upload a .npy file containing your numpy array
   - Create with: `np.save('filename.npy', your_array)`

The image will automatically update when you modify the input.
Note: Values will be automatically scaled to 0-255 range for display.
""")
