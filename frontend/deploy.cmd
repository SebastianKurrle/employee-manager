rd /s /q "dist"
call npm run build
echo "Build ist fertig"

cd dist
git init
git add -A
git commit -m 'deploy'
git remote add origin https://github.com/WastKurrle/emp_manager-deploy.git
git push --force -u https://github.com/WastKurrle/emp_manager-deploy.git
cd ..