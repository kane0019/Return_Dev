def module_dictionary(module_ID):
    module_dictionary={
        
        "RESOURCE_A_MINER":{"Description":"ResourceA miner","energy_change":-1,"resourceA_change":-10,"resourceB_change":-10,"power_change":0,"resourceA_income":20,"resourceB_income":0,"lost_energy_change":1,"lost_power_change":0,"lost_resourceA_income":-20,"lost_resourceB_income":0},
        "GENERATOR":{"Description":"Reactor","energy_change":5,"resourceA_change":-10,"resourceB_change":-10,"power_change":0,"resourceA_income":0,"resourceB_income":0,"lost_energy_change":-5,"lost_power_change":0,"lost_resourceA_income":0,"lost_resourceB_income":0},
        "REFLECT_SHEILD":{"Description":"Reflect Sheild","energy_change":-3,"resourceA_change":-20,"resourceB_change":-10,"power_change":2,"resourceA_income":0,"resourceB_income":0,"lost_energy_change":3,"lost_power_change":-2,"lost_resourceA_income":0,"lost_resourceB_income":0}
    }
    
    return module_dictionary[module_ID]
