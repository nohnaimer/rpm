# Список поддерживаемых операционных систем
```bash
$ go tool dist list
aix/ppc64
android/386
android/amd64
android/arm
android/arm64
darwin/amd64
darwin/arm64
dragonfly/amd64
freebsd/386
freebsd/amd64
freebsd/arm
freebsd/arm64
illumos/amd64
js/wasm
linux/386
linux/amd64
linux/arm
linux/arm64
linux/mips
linux/mips64
linux/mips64le
linux/mipsle
linux/ppc64
linux/ppc64le
linux/riscv64
linux/s390x
netbsd/386
netbsd/amd64
netbsd/arm
netbsd/arm64
openbsd/386
openbsd/amd64
openbsd/arm
openbsd/arm64
plan9/386
plan9/amd64
plan9/arm
solaris/amd64
windows/386
windows/amd64
windows/arm
```
# Сборка agent
```bash
$ git clone git@github.com:nohnaimer/agent.git
$ cd agent
$ env GOOS=linux GOARCH=amd64 go build -v . # Для linux x86_64
$ env GOOS=solaris GOARCH=amd64 go build -v . # Для solaris x86_64
```
# Создание spec файла. Полезные ссылки:
```link
http://wiki.rosalab.ru/ru/index.php/Сборка_RPM_-_быстрый_старт
http://ftp.rpm.org/max-rpm/s1-rpm-build-creating-spec-file.html
```
# Создание архива tgz
```bash
$ tar -czf agent-0.0.3.tgz agent-0.0.3
```