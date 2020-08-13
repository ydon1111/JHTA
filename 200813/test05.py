from pathlib import Path


# Path("./img/test").mkdir(exist_ok=True) #폴더가 없으면 폴더를 만듬
Path("./img/aaa/bbb/ccc/test").mkdir(parents=True, exist_ok=True) #상위폴더가 없으면 상위폴더도 만듬 