# -----------------------------------------------------#
#                       Project rename                 #
# -----------------------------------------------------#
# """ Rename the project name, imports, docs, etc.

#     Credits:
#     Abner G Jacobsen
#     https://github.com/abnerjacobsen
# """
find . -type f -exec sed -i 's/Curso_FastAPI_Template_Backend/change-me/g' {} +
find . -type f -exec sed -i 's/curso_fastapi_template_backend/change_me/g' {} +

find . -type d -name 'curso_fastapi_template_backend' | while read FILE ; do
    newfile="$(echo ${FILE} |sed -e 's/curso_fastapi_template_backend/change_me/')" ;
    mv "${FILE}" "${newfile}" ;
done

find . -type d -name 'Curso_FastAPI_Template_Backend' | while read FILE ; do
    newfile="$(echo ${FILE} |sed -e 's/Curso_FastAPI_Template_Backend/change-me/')" ;
    mv "${FILE}" "${newfile}" ;
done

rm -f .git/index
git reset

