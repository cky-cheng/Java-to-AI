def filter_valid(skills: list[str | None]) -> list[str]:
    # 过滤掉 None 和 空字符串
    result: list[str] = []
    for skill in skills:
        if not skill:
            continue
        result.append(skill)
    return result

def score_job(salary_min: int, salary_max: int) -> int:
    # 薪资区间中点，整数返回
    return (salary_min + salary_max) // 2

def greet(name: str, greeting : str = "你好") -> str:
    return f"{greeting}, {name}"

print(filter_valid(["Python", None, "", "RAG", "  "]))
print(score_job(12, 20))
print(greet("Kory"))
