from scs4onnx import shrinking

shrunk_graph, npy_file_paths = shrinking(
  input_onnx_file_path=r'C:\Users\Biancaa. R\rpi_disease\pest_classification\model1.onnx',
  output_onnx_file_path='shrink.onnx',
  mode='npy',
  non_verbose=True
)

#  'npy': Outputs constant values used repeatedly in the model to an external file .npy.
#Instead of the smallest model body size, the file loading overhead is greater.
#Default: shrink