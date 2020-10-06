from deeppavlov import configs
from deeppavlov.core.common.file import read_json

new_config=read_json('gobot_dstc2_best.json')

from deeppavlov.utils.telegram import interact_model_by_telegram

interact_model_by_telegram(model_config=new_config, token={TOKEN})
