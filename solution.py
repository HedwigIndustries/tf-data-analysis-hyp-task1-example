from scipy import stats

chat_id = 886180056


def solution(x_success: int,
             x_cnt: int,
             y_success: int,
             y_cnt: int) -> bool:
    z_stat, p_value = stats.proportions_ztest([x_success, y_success], [x_cnt, y_cnt], alternative='two-sided')
    alpha = 0.08
    return p_value < alpha
