-- 계열이 '공학'인 학과 중 입학정원이 20이상, 30이하인 학과의 계열, 학과이름, 정원을 조회하시오
-- 단 학과이름을 기준으로 오름차순 정렬
SELECT category, department_name, capacity
FROM tb_department
WHERE capacity BETWEEN 20 AND 30 AND category = '공학'
ORDER BY 2;

-- '학'자가 들어간 계열의 소속 학과가 몇 개 있는지 계열별, 학과 수를 출력하시오.
-- 단, 학과 수가 많은 순으로 정렬하시오.
SELECT category, COUNT(*) AS "학과 수"
FROM tb_department
GROUP BY category
HAVING category LIKE '%학%'
ORDER BY "학과 수" DESC;

-- '영어영문학과' 교수이름, 출생년도, 주소를 조회하고 나이가 많은 순으로 정렬하시오.
SELECT professor_name AS "이름", SUBSTR(professor_ssn, 1, 2) AS "출생년도", professor_address AS "주소"
FROM tb_professor
WHERE department_no = 
(SELECT department_no
FROM tb_department
WHERE department_name = '영어영문학과')
ORDER BY 2;

-- 국어국문학과 학생 중 서울에 거주하는 학생의 학과번호, 학생이름, 휴학여부를 조회하고 학생이름으로 오름차순 정렬하시오.
-- 단, 휴학여부는 값이 'Y'이면 '휴학'으로 'N'이면 '정상'으로 출력한다.
-- 국어국문학과 코드는 TB_DEPARTMENT에서 찾는다.
SELECT department_no AS "학과번호", student_name AS "학생이름",  
CASE WHEN absence_yn = 'Y' THEN '휴학'
WHEN absence_yn = 'N' THEN '정상'
END AS  "휴학여부"
FROM tb_student
WHERE department_no = (
SELECT department_no
FROM tb_department
WHERE department_name = '국어국문학과')
AND student_address LIKE '%서울%'
ORDER BY 2;

-- 80년생인 여학생 중 성이 '김'씨인 학생의 주민번호, 학생이름을 조회하시오.
-- 학생이름으로 오름차순 정렬, 주민번호 -> [주민번호]로 표시
SELECT '[' || SUBSTR(student_ssn, 1, 8) || '******]' AS "주민번호", student_name AS "이름"
FROM tb_student
WHERE SUBSTR(student_ssn, 8, 1) = '2' AND
SUBSTR(student_name, 1, 1) = '김' AND
SUBSTR(student_ssn, 1, 2) = '80';

-- 계열이 '예체능'인 학과의 정원을 기준으로 40이상이면 '대강의실' 30이사이면 '중강의실'
-- 나머지는 '소강의실'로 출력한다. 단, 정원이 많은 순으로 정렬한다
SELECT department_name AS "학과이름", capacity AS "현재정원",
CASE WHEN capacity >= 40 THEN '대강의실'
WHEN capacity >= 30 THEN '중강의실'
ELSE '소강의실'
END AS "강의실크기"
FROM tb_department
WHERE category = '예체능'
ORDER BY 2 DESC;
