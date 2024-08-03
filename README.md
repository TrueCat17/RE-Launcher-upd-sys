# RE-Launcher-upd-sys

## \[ru]

Репозиторий для обновления Лаунчера движка Ren-Engine (под технические нужды).

#### Обновление

1. Добавить zip-файл в `zips`: последний zip (по mtime, не меняется при копировании) - текущая версия;
2. Запустить `./update.py`.

Новые/изменённые файлы: `update_number.txt` и `info.txt`.  
Папка `files` с распакованными файлами.

#### Номер обновления

`update_number.txt` содержит число, увеличивающееся на 1 после каждого обновления.  
Служит минималистичным индикатором того, что было сделано обновление.

#### Информация

`info.txt` содержит строки для каждого файла в формате `путь`|`sha256`|`размер`.  
Путь папок всегда заканчивается разделителем, разделитель всегда является символом `/` (и никогда - `\`).  
Хэш отсутствует у папок и удалённых файлов.  
Размер директорий - `0`, размер удалённых файлов и папок - отсутствует.

Хранение путей удалённого содержимого нужно, чтобы при обновлении движок мог точно знать,
какие файлы нужно удалить, а какие стоит оставить, даже если о них ничего не сказано.  
Это может быть полезно, например, для игнорирования (а не удаления) модов.

#### Скачивание

Использование zip-архива удобно сразу в 2 смыслах:
1. Можно давать ссылку на скачивание архива (на гитхабе - через `raw.githubusercontent.com`);
2. Нельзя забыть удалить предыдущие файлы перед обновлением (это делается автоматически).

Движок же при обновлении будет скачивать только новые файлы (с изменёнными хэшами), распакованные скриптом в `files`.  
В результате для обновления нужно будет скачать (зачастую) меньше 1 МБ, а не полный архив на десятки МБ.




## \[en]

Repository for updating Launcher of Ren-Engine (for technical needs).

#### Updating

1. Add zip-file to `zips`: latest zip (by mtime, does not change when copied) is a current version;
2. Start `./update.py`.

New/changed files: `update_number.txt` and `info.txt`.  
Dir `files` with unpacked files.

#### Number of update

`update_number.txt` contains a number that increases by 1 after each update.  
Serves as a minimalistic indicator that an update has been made.

#### Info

`info.txt` contains lines for each file in the format `path`|`sha256`|`size`.  
The hash is missing for dirs and deleted files.  
The size of dirs is `0`, the size of deleted files and dirs is missing.

Storing the paths of deleted content is necessary so that when updating the engine can know exactly
which files need to be deleted and which should be left, even if nothing is said about them.  
This can be useful, for example, for ignoring (rather than removing) mods.

#### Downloading

Using a zip archive is convenient in two ways:
1. You can provide a link to download the archive (on github - via `raw.githubusercontent.com`);
2. You cannot forget to delete previous files before updating (this is done automatically).

When updating, the engine will download only new files (with changed hashes), unpacked by the script into `files`.  
As a result, to update you will need to download (often) less than 1 MB, and not a full archive of tens of MB.
