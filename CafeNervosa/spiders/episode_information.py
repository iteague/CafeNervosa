import scrapy 

class EpisodeInformation(scrapy.Spider):
	name = 'episodes'
	allowed_domains =['frasieronline.co.uk']
	start_urls = [
		'http://www.frasieronline.co.uk/episodeguide/'
	]
	
	def parse(self, response):
		
		seasons = response.xpath("//tr//p[1]/a/@href").extract()	
		
		for season in seasons:
			episodePage = response.urljoin(season)
			yield scrapy.Request(episodePage, callback=self.parse_season)
			
	def parse_season(self, response):
		
		def extract_with_xpath(query):
			return response.xpath(query).extract()
			
		yield {
			'Page Title': extract_with_xpath("head/title/text()"),
			'Episodes': extract_with_xpath("//td[@class='epguide_Title']/a/text()")

		}
		
		


			
		

