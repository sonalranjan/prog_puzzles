
# https://app.codesignal.com/arcade/python-arcade/higher-order-thinking/mxSa4di775kRL26bW

def solution(vines, n):
    def nTimes(n):
        def deco_repeat(func):
            return functools.reduce(lambda f,g: functools.partial(lambda v: f(g(v))), [func]*n) if n > 0 else lambda v: v
        return deco_repeat
                
    @nTimes(n)
    def sumOnce(vines):
        res = [vines[i] + vines[i + 1] for i in range(0, len(vines) - 1, 2)]
        if len(vines) % 2 == 1:
            res.append(vines[-1])
        return res

    return sumOnce(vines)
