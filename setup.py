import setuptools

setuptools.setup(
    name="CheckHustBalance",
    version="1.0",
    author="chenyucheng0503",
    author_email="1731354527@qq.com / grahamsa0503@gmail.com",
    description="用于查询和充值华中科技大学饭卡",
    url="https://github.com/chenyucheng0503/CheckHustBalance",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    setup_requires=["pillow", "pytesseract", "pytest-runner"],
    tests_require=["pytest"],
    python_requires=">=3.6",
    test_suite="tests"
)