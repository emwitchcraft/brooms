def paramGen(layer, totalLayers, steps, start, stop):
    inc = (stop - start) / (steps - 1)
    val = start
    counter = 0
    counterMax = totalLayers ** steps
    counterThresh = steps ** (layer)
    while counter < counterMax:
        yield val
        counter += 1
        if counter % counterThresh == 0:
            val += inc
            if val > stop:
                val = start
            
#params is list of tuples (name, start, stop)
def generateParamGens(params: list, steps):
    paramGens = {param[0]: paramGen(i, len(params), steps, param[1], param[2]) for i,param in enumerate(params)}
    return paramGens
    
def sweep (function, params, steps):
    paramGen = generateParamGens(params, steps)
    while 1:
        try:
            paramSet = {param: next(value) for param,value in paramGen.items ()}
            function(paramSet)
        except StopIteration:
            break

if __name__ == '__main__':
    def function(paramSet):
        p1 = paramSet['p1']
        p2 = paramSet['p2']
        p3 = paramSet['p3']
        print(f'{p1}\t{p2}\t{p3}')

    params = [('p1', 0, 2), ('p2', 0, 2), ('p3', 0, 2)]
    sweep(function, params, 3)
