def solution(id_list, report, k):
    answer = [0]*len(id_list)

    reported_dict = {id: 0 for id in id_list} # 신고당한 이름 : 신고 당한 횟수
    reporter_dict = {id: 0 for id in id_list} # 신고한 이름 : 메일 받은 횟수
    
    report = list(set(report)) # 동일 신고 중복 제거
    # print('report', report)
    
    for r in report:
        reporter, reported = r.split()
        reported_dict[reported] += 1
        
    # print('reported_dict', reported_dict)
    
    for r in report:
            reporter, reported = r.split()
            if reported_dict[reported] >= k:
                reporter_dict[reporter] += 1
                
    answer = list(reporter_dict.values())
    
    return answer