class CreateExampleTable < ActiveRecord::Migration[7.1]

  def change

    create_table :example_table do |t|

      t.string :name

      t.date :date_of_birth  # Remplacement de "age" par "date_of_birth"

      t.string :pays         # Ajout de la colonne "pays"

      t.string :adresse      # Ajout de la colonne "adresse"

      t.timestamps

    end

  end

end

 

class CreateNezTable < ActiveRecord::Migration[7.1]

  def change

    create_table :nez_table do |t|

      t.integer :example_table_one_id  # Première référence à example_table

      t.integer :example_table_two_id  # Deuxième référence à example_table

      t.string :fake_data              # Colonne pour des données factices

      t.timestamps

    end

  end

end

 

require 'faker'

 

nez_entry = NezTable.create(

  example_table_one_id: 1,

  example_table_two_id: 2,

  fake_data: Faker::Lorem.sentence

)

 

puts nez_entry.fake_data  # Affiche une phrase générée aléatoirement

 

require 'nokogiri'

require 'open-uri'

require 'countries'

 

url = "https://www.bing.com/news"

page = Nokogiri::HTML(URI.open(url))

 

# Liste complète des pays

pays = Country.all.map(&:name)

 

# Liste complète des sports

sports = [

  "football", "tennis", "rugby", "basketball", "natation", "cyclisme", "athlétisme", "boxe",

  "judo", "karaté", "taekwondo", "hockey", "volleyball", "escrime", "handball", "golf",

  "surf", "canoë-kayak", "plongée", "ski", "motocross", "parkour", "équitation"

]

 

page.css('.news-card').each do |article|

  titre = article.css('.title').text.strip

  contenu = article.css('.snippet').text.strip

  

  pays_mentionnes = pays.select { |p| titre.include?(p) || contenu.include?(p) }

  mentions_sport = sports.any? { |sport| titre.downcase.include?(sport) || contenu.downcase.include?(sport) }

 

  if pays_mentionnes.any?

    type_article = mentions_sport ? "Sport" : "Autre"

 

    # Sélection aléatoire d'un nombre de pays

    pays_random = pays.sample(pays_mentionnes.count)

 

    titre_modifie = titre.dup

    contenu_modifie = contenu.dup
 
 

    pays_mentionnes.each_with_index do |pays, index|

      titre_modifie.gsub!(pays, pays_random[index])

      contenu_modifie.gsub!(pays, pays_random[index])

    end

 

    puts "Titre : #{titre_modifie} (Pays remplacés : #{pays_mentionnes.count})"

    puts "Contenu : #{contenu_modifie}"

    puts "Catégorie : #{type_article}"

    puts "-" * 50

  end

end

