import os

trainCommand = """
python run_training.py \
  --work-dir /DATA/anivray/output3 \
  data:custom \
  --data.data-dir /DATA/anivray/taxi2
"""

renderCommand = """
python run_rendering.py \
  --work-dir /DATA/anivray/output \
"""

os.system(renderCommand)
