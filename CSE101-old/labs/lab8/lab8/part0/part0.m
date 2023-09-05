in_file = fopen('aFile.txt', 'r');

if in_file == -1
    error('oops, file can''t be read'); 
end 

line = fgetl( in_file );

disp(line);

fclose(in_file);