# 安装 Homebrew（如果未安装）
if ! command -v brew &>/dev/null; then
  echo "Homebrew 未安装。正在安装 Homebrew..."
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

# 安装 pyenv 和 pyenv-virtualenv
brew update
brew install pyenv pyenv-virtualenv

# 安装 Python 3.12.2
pyenv install 3.12.2
pyenv global 3.12.2

# 重新加载 shell
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

# 添加 pyenv 到环境变量
echo -e '\n# Pyenv configuration' >> ~/.zprofile
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zprofile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zprofile
echo 'eval "$(pyenv init --path)"' >> ~/.zprofile
echo 'eval "$(pyenv init -)"' >> ~/.zprofile
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zprofile
source ~/.zprofile

# 确认安装
python --version
