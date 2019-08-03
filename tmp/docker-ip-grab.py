#! python
import subprocess
import re
import jinja2

pattern = r'(?<= )\w*$'
lst = []
dic = {}

if __name__ == "__main__":
    out = subprocess.getoutput("docker ps | tail -n +2")
    for x in out.split("\n"):
        lst.append(re.findall(pattern, x)[0])
    for container in lst:
        dic[container] = subprocess.getoutput(
            "docker inspect -f '{{ range .NetworkSettings.Networks }}{{.IPAddress}}{{end}}' " + container
        )

    fileloader = jinja2.FileSystemLoader('/home/yharwyn-/Templates')
    env = jinja2.Environment(loader=fileloader)
    template = env.get_template('hosts.j2')

    output = template.render(data=dic)
    with open("hosts-j2", "w") as f:
        f.write(output)
    print(dic)
