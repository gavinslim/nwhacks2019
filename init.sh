echo 'Cleanup img dir'
rm get_faceapi/imgs/*.jpg

echo 'Init AdSight service'

python local-vision.py

function finish {
  killall python
}
trap finish EXIT
