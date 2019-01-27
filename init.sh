echo 'Cleanup img dir'
rm *.jpg

echo 'Init AdSight service'

python3 local-vision.py

function finish {
  killall python
}
trap finish EXIT
