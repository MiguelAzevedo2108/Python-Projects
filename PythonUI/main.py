from ipywidgets import interact, interactive,fixed
import ipywidgets as widgets

def func(x):
    return x

if __name__ == '__main__':
    x = interact(func,x=True)
    print('PyCharm')
