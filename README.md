To build the n8n version theat is supported by PI2 we need to build out own from the n8n git repo

docker buildx create --name mybuilder --use
docker buildx inspect --bootstrap

cd ~
git clone https://github.com/n8n-io/n8n.git
cd n8n

docker buildx build --platform linux/arm/v7 -t n8n-arm32 .





git init
git remote add origin git@gitlab.com:mjbejaranob/n8n-raspi.git
# or use https: https://gitlab.com/<username>/<project>.git (you'll be prompted for credentials)
git clone https://gitlab.com/mjbejaranob/n8n-raspi.git