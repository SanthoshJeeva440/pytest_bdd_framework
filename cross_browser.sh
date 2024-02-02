echo "Cross Browser Test"

echo "Chrome Browser"
pytest --headmode "headless" --template=html1/index.html --report=test-results/cross-browser/chrome.html
sleep 10

echo "Edge Browser"
pytest --headmode "headless" --browser "edge" --template=html1/index.html --report=test-results/cross-browser/edge.html
sleep 10

echo "Firefox Browser"
pytest --headmode "headless" --browser "firefox" --template=html1/index.html --report=test-results/cross-browser/ff.html