sudo ﻿ln -s /home/box/web/stepic_web_project/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/stepic_web_project/etc/gunicorn.conf   /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart
﻿sudo /etc/init.d/mysql start﻿
