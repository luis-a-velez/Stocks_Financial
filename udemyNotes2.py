"""
Example: Imagine you bought 1 share of Facebook 
(FB) for $160, and 1 share of Apple 
(AAPL) for $180.
What is your profit & return if you sold FB for 
$172.47 and AAPL for $188.83?
"""

"""Profit?"""
Your profit would be $21.30
$172.47 − $160 + $188.83 − $180
(P FB,t+1 - P FB,t) + (P AAPL, t+1 - P AAPL,t)

"""Returns?"""
""" Your return on FB would be 7.79%; and 
AAPL would be 4.91%
rFB = (P FB,t+1 / P FB, t) - 1 ===> (172.47 / 160) - 1 =~ 0.0779
DO AAPL:
"""

"""Perfolio Returns?"""
""" 
Although FB’s return is 7.79% you only 
invested approximately 47% of your 
money in FB; not 100%.
Proportion in FB =
Proportion in FB = 160 / (160+180) ≈ 0.4706
"""
""" 
Essentially, you only earn approximately 
47% of the 7.79% return (i.e. 3.67%)
Share of FB return = 0.4706 × 0.0779 ≈ 0.0367.

Similarly, your ‘share of return’ from AAPL 
is approximately 2.6%
Share of AAPL return =
180 / (160+180) × 0.0491 ≈ 0.026
"""
""" 
In total, your portfolio earned 6.27%.
Share of FB return + Share of AAPL return
($160 / $160 + $180) 0.0779 + ($180 / $160 + $180) 0.0491 = 0.062.

"""
""" Portfolio Return Formula """
""" ($160 / $160 + $180) 0.0779 + ($180 / $160 + $180) 0.0491 = 0.062.
        Wfb       *       rFB   +        WAAPL      *      rAAPL 
Wfb = weights for FACEBOOK
rfb = Returns for FACEBOOK
WAAPL = weights for FACEBOOK
rAAPL = Returns for FACEBOOK



"""
