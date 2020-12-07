def minimum_distance(points):

    sorted_p_x = sorted(points, key=lambda p: p.x)



    return large_size_min_distance(sorted_p_x)



def small_size_min_distance(points):

    result = sys.maxsize

    for i in range(len(points)):

        for j in range(i+1, len(points)):

            result = min(result, distance(points[i], points[j]))

    return result



def large_size_min_distance(p_x):

    size = len(p_x)

    half_size = int(len(p_x)/2)



    if size <= 3:

        return small_size_min_distance(p_x)



    left_p_x = p_x[0:half_size]

    right_p_x = p_x[half_size:size]



    left_min = large_size_min_distance(left_p_x)

    right_min = large_size_min_distance(right_p_x)

    separated_min = min(left_min, right_min)



    line_l = (left_p_x[-1].x + right_p_x[0].x)/2

    hybrid_min = compute_hybrid_min(left_p_x, right_p_x, line_l, separated_min)



    return min(separated_min, hybrid_min)