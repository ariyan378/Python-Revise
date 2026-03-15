information = {
    
    'numpy': "Mathmatics",
    'pandas':"Explore dataset",
    'seborn':'Visualization',
    'pytorch':'Deep Learning'
}

for i, (name ,task) in  enumerate(information.items() , 1):
    print(f'{i}.{name} Task {task}')