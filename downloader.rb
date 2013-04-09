require "mechanize"

url   = "http://kemahasiswaan.um.ac.id/?p=6651"
agent = Mechanize.new
page  = agent.get(url)

doc_xpath = '//div[@class="post-entry"]//a[contains(@href,"/wp-content/uploads/")]/@href'
links = page.search(doc_xpath).map(&:text)

links.each do |link|
  puts "saving #{link}"
  agent.get(link).save
end
