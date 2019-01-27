echo 'Cleanup img dir'
rm get_faceapi/imgs/*.jpg

echo 'Init AdSight service'

python local-vision.py

function finish {
  pkill -f local-vision.py
}
trap finish EXIT
