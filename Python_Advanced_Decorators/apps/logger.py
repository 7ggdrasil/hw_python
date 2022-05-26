import time

def logger1(func):
    log = {}    
    def foo_logger(*args, **kwargs):
        timekey = time.strftime("%d.%m.%Y г. %H:%M", time.localtime())        
        result = func(*args, **kwargs)
        log[timekey] = f'{func.__name__}, {args}, {result}'
        with open('log.txt','a', encoding="utf-8") as f:
            f.write(str(log))
        return result    
    return foo_logger

def logger2(path):
    def logger(func):
        log = {}    
        def foo_logger(*args, **kwargs):
            timekey = time.strftime("%d.%m.%Y г. %H:%M", time.localtime())        
            result = func(*args, **kwargs)
            log[timekey] = f'{func.__name__}, {args}, {result}'
            with open(path,'a', encoding="utf-8") as f:
                f.write(str(log))
            return result    
        return foo_logger
    return logger