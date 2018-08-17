make clean
make html
ls
cd docs/html
git init
git add .
git commit -am "Automatic Commit"
git push -f git@github.com:sagelga/monopoly-analysis.git master:gh-pages
cd ../../
