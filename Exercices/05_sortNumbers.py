numbers = [328,156,938,903,708,435,420,770,439,162,574,601,625,632,627,349,62,587,518,405,621,682,40,835,36,70,830,768,622,187,984,213,475,167,100,875,945,85,97,392,791,658,800,674,269,378,882,322,324,531,227,660,99,843,170,954,670,332,128,345,356,280,396,900,104,215,643,579,285,234,855,789,91,569,975,549,527,548,473,18,612,709,537,781,74,538,878,628,996,681,525,437,558,343,184,81,98,646,63,888,504,458,44,490,60,390,330,782,147,131,287,255,77,483,616,831,281,599,872,71,535,937,606,90,367,836,83,366,121,635,930,211,603,369,45,732,694,261,655,380,220,551,656,816,961,23,20,698,276,745,1000,297,570,556,809,318,226,247,725,182,914,560,942,676,542,350,513,990,973,840,196,691,9,153,6,896,714,355,368,228,931,739,593,776,351,283,941,183,617,786,607,710,145,668,881,750,404,993,586,382,102,19,177,623,526,123,948,57,916,462,774,803,982,833,976,939,362,1,697,901,837,305,726,260,429,692,927,242,389,647,523,767,190,35,497,545,181,883,662,137,417,540,3,315,342,264,363,754,101,985,105,520,321,756,50,686,428,822,790,294,921,547,673,150,636,365,159,199,505,738,970,66,834,981,408,108,711,651,311,755,983,764,141,364,907,416,706,918,811,86,78,544,395,432,521,839,639,753,890,256,951,410,876,168,166,509,142,243,291,333,580,685,259,829,847,300,359,687,730,934,55,654,219,924,735,864,591,110,476,503,661,704,489,859,360,724,573,479,817,998,472,826,65,82,806,536,741,910,12,846,775,824,841,828,299,16,644,225,348,301,891,582,232,892,577,399,188,73,913,25,387,642,604,702,120,132,84,339,265,971,143,857,442,400,514,419,596,894,191,440,815,696,271,302,251,189,484,950,53,804,889,492,54,26,511,313,449,118,615,130,394,246,361,666,282,629,471,779,564,771,671,899,209,346,717,956,327,733,528,312,11,557,838,186,801,424,705,372,344,59,977,426,27,326,7,286,920,995,854,862,138,317,598,650,245,335,175,374,103,649,221,539,306,721,92,79,805,529,107,409,980,933,268,337,195,401,851,34,749,566,960,422,852,630,515,2,229,433,457,559,414,652,296,718,194,955,452,760,8,926]

def is_sorted(array):
    return array == sorted(array)


print(is_sorted(numbers)) # => False
print(is_sorted([1, 2])) # => True

# tips to view a sorted array : sorted(array)