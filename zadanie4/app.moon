lapis = require "lapis"
import respond_to, json_params from require "lapis.application"


lapis = require "lapis"
db = require "lapis.db"
models = require "models"
import Model from require "lapis.db.model"

class Category extends Model
    @primary_key: "name"
  
    name: string
    description: string
  
class Products extends Model
  @primary_key: "name"

  name: string
  description: string
  price: number
  category_name: Category

class App extends lapis.Application
  [category: "/category"]: respond_to {
    GET: => 
      categories = nil
      if @params.name
        categories = Category\find @params.name
      else
        categories = Category\select '*'

      if categories
        {
          json: categories
        }

    POST: json_params =>
      if @json.name 
        category = Category\find @json.name
        if not category
          category = Category\create @json
          @html ->
            h3 "Category created succesfully!"
        else
          @html ->
            h3 "Category already exists!"
      else
        @html ->
          h3 "Not provided category name"
    
    PUT: json_params =>
      category = Category\find @json.name
      if category
        category.description = @json.description
        category\update "description"
      else
        @html ->
          h3 "Category does not exists!"
    
    DELETE: =>
      if @params.name
        category = Category\find @params.name
        if category
          category\delete!
        else
          @html ->
            h3 "Category does not exists!"
      else
        @html ->
          h3 "Not provided category name"
    }

  [products: "/products"]: respond_to {
    GET: => 
      products = nil
      if @params.name
        products = Products\find @params.name
      else
        products = Products\select '*'
      if products
        {
          json: products
        }

    POST: json_params =>

      if not @json.name or not @json.category or not @json.price
        @html ->
          h3 "Missing product informations!"
        return
          
      category = Category\find @json.category

      if not category
        @html ->
          h3 "Category not found!"
        return
      
      product = Products\find @json.name

      if product
        @html ->
          h3 "Product already exists!"
        return
      
      pr = Products\create @json
      @html ->
        h3 "Product created succesfully!"

      
        
    
    PUT: json_params =>
      product = Products\find @json.name

      if product
        product.description = @json.description
        product.price = @json.price
        category = Category\find @json.category

        if category
          product.category = @json.category
          product\update "name", "description", "price", "category"
        else
          @html ->
            h3 "Category does not exists!"
          product\update "name", "description", "price"

      else
        @html ->
          h3 "product does not exists!"
    
    DELETE: =>
      if @params.name
        product = Products\find @params.name
        if product
          product\delete!
        else
          @html ->
            h3 "Product does not exists!"
      else
        @html ->
          h3 "Not provided product name"
    }