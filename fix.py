import os
import shutil

replace_entities='''<a href="tel:+12066474733" class="call-us-button" title="Call Us">
	📞 Click here to call us now +1 (206) 647-4733
	</a>

	<style>
	.call-us-button {
		position: fixed;
		bottom: 20px;
		left: 50%;
		transform: translateX(-50%);
		background-color: red;
		color: white;
		padding: 14px 24px;
		font-size: 16px;
		font-weight: bold;
		border-radius: 50px;
		box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
		text-decoration: none;
		z-index: 1000;
		transition: background-color 0.3s ease;
	}

	

	@media screen and (max-width: 480px) {
		.call-us-button {
		padding: 12px 20px;
		font-size: 14px;
		}
	}
	</style>
<footer
'''

for d in os.listdir('bathroom-remodeling'):
    try:
        for c in os.listdir(f'bathroom-remodeling/{d}'):
            try:
                for b in os.listdir(f'bathroom-remodeling/{d}/{c}'):
                    try:
                        search_categories = open(f'bathroom-remodeling/{d}/{c}/{b}', "r", encoding="utf8").read()
                        
                        op= search_categories.replace("���", "'").replace("<footer", replace_entities)
                        
                        fp = open(f'bathroom-remodeling/{d}/{c}/{b}', "w", encoding='utf-8-sig')
                        fp.writelines(op)
                        fp.close()
                    except:
                        pass
            except:
                pass
    except:
        pass
    
for d in os.listdir('bathroom-remodeling'):
    try:
        search_categories = open(f'bathroom-remodeling/{d}/index.html', "r", encoding="utf8").read()
        
        op= search_categories.replace("���", "'").replace("<footer", replace_entities)
        
        fp = open(f'bathroom-remodeling/{d}/index.html', "w", encoding='utf-8-sig')
        fp.writelines(op)
        fp.close()
    except:
        pass


try:
    search_categories = open(f'bathroom-remodeling/index.html', "r", encoding="utf8").read()
    
    op= search_categories.replace("���", "'").replace("<footer", replace_entities)
    
    fp = open(f'bathroom-remodeling/index.html', "w", encoding='utf-8-sig')
    fp.writelines(op)
    fp.close()
except:
    pass

try:
    search_categories = open(f'index.html', "r", encoding="utf8").read()
    
    op= search_categories.replace("���", "'").replace("<footer", replace_entities)
    
    fp = open(f'index.html', "w", encoding='utf-8-sig')
    fp.writelines(op)
    fp.close()
except:
    pass
