*** Settings ***
Library  OperatingSystem
*** Variables ***
${out_dir} =    outputs
${dir_1} =  first_dir
${dir_2} =  second_dir
${file_1} =  first_file
${file_2} =  second_file
${file_3} =  third_file
*** Test Cases ***
create base directory
    create directory  ${out_dir}
    should exist  ${out_dir}
create Directory 1
    ${dir_path} =   join path  ${out_dir}    ${dir_1}
    create directory  ${dir_path}
    should exist  ${dir_path}
create Directory 2
    ${dir_path} =   join path  ${out_dir}   ${dir_2}
    create directory  ${dir_path}
    should exist  ${dir_path}
create first file
    ${file_path} =  join path  ${out_dir}   ${dir_1}    ${file_1}
    create file  ${file_path}   this is first file
    should exist  ${file_path}
create second file
    ${file_path} =  join path  ${out_dir}   ${dir_2}    ${file_2}
    create file  ${file_path}   this is second file
    should exist  ${file_path}
create third file
    ${file_path} =  join path  ${out_dir}   ${dir_2}    ${file_3}
    create file  ${file_path}   this is third file
    should exist  ${file_path}
move file 3 from directory 2 to directory 1
    ${source_path} =    join path  ${out_dir}   ${dir_2}    ${file_3}
    ${target_path} =    join path  ${out_dir}   ${dir_1}    ${file_3}
    move file  ${source_path}   ${target_path}
copy file 3 from directory 1 to directory 2
    ${source_path} =    join path  ${out_dir}   ${dir_1}    ${file_3}
    ${target_path} =    join path  ${out_dir}   ${dir_2}    ${file_3}
    copy file   ${source_path}   ${target_path}




