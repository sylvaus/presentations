#include <memory>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

class POD;
double internal_method(POD* pod) {};

double compute_complex_value_98(POD* pod)
{
    double result = 0;

    // Some computation

    // By this point another thread could have thread the
    // pointer to pod

    result += internal_method(pod);

    // more computations

    // Are we supposed to delete pod ?
    return result;
}

double compute_complex_value_11(shared_ptr<POD> pod)
{
    double result = 0;

    // Some computation

    // No thread will have deleted pod
    // since we hold a reference

    result += internal_method(pod.get());

    // more computations

    // Pod way be deleted after we return the function
    // if we had the last reference
    return result;
}

struct Article
{
    string name;
    uint64_t quantity;
    Article(string name, uint64_t quantity):
        name(move(name)), quantity(quantity) {}
};

struct ArticleReference
{
    weak_ptr<Article> article;
    string name;

    explicit ArticleReference(const shared_ptr<Article>& article):
        article(article), name(article->name) {}
};

class Order
{
public:
    void add_article(const ArticleReference& article)
    {
        articles_.push_back(article);
    }

    void list_articles()
    {
        for (const auto& article_ref: articles_)
        {

            if (auto article = article_ref.article.lock())
                cout << "Article " << article->name
                     << " has " << article->quantity << "left" << endl;
            else
                cout << "Article " << article_ref.name
                     << " does not exist anymore" << endl;
        }

        auto is_expired = [](const ArticleReference& ref){return ref.article.expired();};
        auto start = remove_if(articles_.begin(), articles_.end(), is_expired);
        articles_.erase(start, articles_.end());
    }
private:
    vector<ArticleReference> articles_;
};


int main()
{
    auto shampoo = make_shared<Article>("Shampoo", 10u);
    auto tea = make_shared<Article>("Tea", 25u);
    auto novel = make_shared<Article>("Novel", 12u);

    auto order = Order();
    order.add_article(ArticleReference{shampoo});
    order.add_article(ArticleReference{tea});
    order.add_article(ArticleReference{novel});

    order.list_articles();
    cout << "Tea is no more a product being sold" << endl;
    tea.reset(); // no more tea being sold
    order.list_articles();

    /* Printed
    Article Shampoo has 10left
    Article Tea has 25left
    Article Novel has 12left
    Tea is no more a product being sold
    Article Shampoo has 10left
    Article Tea does not exist anymore
    Article Novel has 12left
     */
}

