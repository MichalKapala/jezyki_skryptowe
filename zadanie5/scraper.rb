require 'nokogiri'
require 'open-uri'

title_classes = [".a-size-base-plus", ".a-size-medium"]

$headers = {}
$headers["User-Agent"] = "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)"
$headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"

category = "electronics"
key_word = ["Iphone", "14", "pro"]
url = "https://www.amazon.pl/s?k=#{key_word.join("+")}&i=#{category}"



def print_table_data(node_set)
    return if node_set.empty?
    node_set.search('tr').each do |row|
        label_cell, value_cell = row.search('td')
        label = label_cell.at('span').text
        value = value_cell.at('span').text
        puts "#{label}: #{value}"
    end
end

def get_details(url)
    url_base = "https://www.amazon.pl"
    doc = Nokogiri::HTML(URI.open(url_base + url, $headers))

    expander_content = doc.css('.a-section')
    specs = expander_content.css('.a-section.a-spacing-small.a-spacing-top-small')
    table_rows = specs.search('table')
    print_table_data(table_rows)
    puts "URL : #{url_base + url}"
  end


puts "Start sraping #{url}"


page = Nokogiri::HTML(URI.open(url, $headers))

page.css('.s-result-item').each do |product|
    title_classes.each do |title_class|
        link = product.css(".a-link-normal")[0]
        title = product.css("#{title_class}").text
        price = product.css('.a-price-whole').text
        if !price.empty? and !title.empty?
            puts "Title: #{title}"
            puts "Price: #{price} PLN"
            get_details(link["href"])
            puts ""
            puts "**********************************************************"
            puts ""
        end
    end
  end