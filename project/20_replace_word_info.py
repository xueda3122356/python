import docx
import os

infos = [
    ['00001', 2030, 12, 12, 12, 0, '闯红灯', 300],
    ['00002', 2031, 12, 12, 12, 0, '违反禁令', 300],
    ['00003', 2032, 12, 12, 12, 0, '违章停车', 300],
]

for info in infos:
    doc1 = docx.Document('./base_data/traffic_violation_notice.docx')
    for p in doc1.paragraphs:
        for run in p.runs:
            run.text = p.text.replace('{0}', info[0])
            run.text = p.text.replace('{1}', str(info[1]))
            run.text = p.text.replace('{2}', str(info[2]))
            run.text = p.text.replace('{3}', str(info[3]))
            run.text = p.text.replace('{4}', str(info[4]))
            run.text = p.text.replace('{5}', str(info[5]))
            run.text = p.text.replace('{6}', info[6])
            run.text = p.text.replace('{7}', str(info[7]))
            # 注意：样式是保存在run里面，不是在p。所以想要保存样式需要保存run
    
    if not os.path.exists('./generate_data/generate_word'):
        os.makedirs('./generate_data/generate_word')
    doc1.save(f'./generate_data/generate_word/20_traffic_violation_notice_{info[0]}.docx')