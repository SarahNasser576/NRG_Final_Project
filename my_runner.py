import os

trainCommand = """
python run_training.py \
  --work-dir /DATA/anivray/output4 \
  data:custom \
  --data.data-dir /DATA/shared/taxi
"""

renderCommand = """
python run_rendering.py \
  --work-dir /DATA/anivray/output \
"""

os.system(trainCommand)
