names = ["Meenakshi","kuldeep","atharv","purohit","Meena"]
#M_names = []
#for name in names:
    #if "M" in name:
        #M_names.append(name)


M_names = [name for name in names if "M" in name]
print(M_names)
