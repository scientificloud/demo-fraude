echo "========== Executando aplicação =========="
cd interface-fraude/
if [ ! -d demo-fraude/ ]; then
    echo "Aplicação não existe no servidor, clonando repositório git."
    git clone https://github.com/scientificloud/demo-fraude.git

    echo "=============================="
    echo "Arquivos clonados com sucesso!"
    echo "=============================="
fi

cd demo-fraude/
git pull origin master
echo "====================="
echo "Arquivos atualizados!"
echo "====================="

cd Flask/

echo "===================="
echo "Executando servidor!"
echo "===================="

python main.py
