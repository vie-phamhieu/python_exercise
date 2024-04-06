# python_exercise
## Cách push code lên github
### Tạo repo trên github
###  Đẩy code lên repo
#### Khởi tạo một repo
```
git init
```
#### Liên kết repo
```
git remote add origin <URL của Repository GitHub>
```
#### Thêm tất cả các tệp và thư mục trong thư mục của bạn vào Repository
```
git add .
```
#### Commit các thay đổi
```
git commit -m 'Commit'
```
#### Đẩy code lên github
```
git push -u origin <Branch>
```
#### Đồng bộ hóa code trước khi push
```
git pull origin <Branch>
```
#### rebase ( cần thực hiện nếu cùng branch nhưng có sự khác nhau giữa file trên github và local )
```
git pull --rebase origin <Branch>
```
## Xem bài tập tại file [exercise.txt](https://github.com/vie-phamhieu/python_exercise/blob/main/exercise.txt)
