#include <iostream>

using namespace std;

//native Order class
class NativeOrder{
public:
	void SetQty(const int order_qty)
	{
		this->order_qty = order_qty;
	}
	void SetPrice(const double price)
	{
		this->price = price;
	}
	void SetInstrumentId(const int instrument_id)
	{
		this->instrument_id = instrument_id;
	}
	void SetExchangeId(const std::string exchange_id)
	{
		this->exchange_id = exchange_id;
	}
	void ShowOrderParams()
	{
		std::cout << "OrderQty:\t" << this->order_qty 
			<< "\norder_price:\t" << this->price
			<< "\ninstrument_id:\t" << this->instrument_id
			<< "\nexchange_id:\t" << this->exchange_id;
	}
	~NativeOrder() = default;
private:
	int order_qty;
	double price;
	int instrument_id;
	std::string exchange_id;
};

class OrderBuilder{
public:
	virtual void BuildOrderQty(const int order_qty) 		= 	0;
	virtual void BuildOrderPrice(const int order_price)  	= 	0;
	virtual void BuildInstrumentId(const int instrument_id)	= 	0;
	virtual void BuildExchangeId(const std::string exchange_id) 		= 	0;
	virtual NativeOrder* GetOrder() 			= 	0;
	virtual ~OrderBuilder() = default;
};

//NativeOrderBuilder which will build the limit order, similar to this
//we can have marketOrderBuilder class, which will only build the market order
class NativeOrderBuilder: public OrderBuilder{
public:
	NativeOrderBuilder()
	{
		order = new NativeOrder();
	}

	void BuildOrderQty(const int order_qty) override
	{
		order->SetQty(order_qty);
	}
	void BuildOrderPrice(const int order_price) override
	{
		order->SetPrice(order_price);
	}
	void BuildInstrumentId(const int instrument_id) override
	{
		order->SetInstrumentId(instrument_id);
	}
	void BuildExchangeId(const std::string exchange_id) override
	{
		order->SetExchangeId(exchange_id);
	}
	NativeOrder* GetOrder() override
	{
		return order;
	}

	~NativeOrderBuilder() = default;
private:
	NativeOrder* order;
};

//use the Orderbuilder interface to construct an order
class OrderBuilderManager{
public:
	void SetOrderBuilder(OrderBuilder* ob)
	{
		order_builder = ob;
	}

	NativeOrder* GetAndCreateOrder(const int order_qty, const double order_price, const int instrument_id, const std::string exchange_id)
	{
		order_builder->BuildOrderQty(order_qty);
		order_builder->BuildOrderPrice(order_price);
		order_builder->BuildInstrumentId(instrument_id);
		order_builder->BuildExchangeId(exchange_id);
		return order_builder->GetOrder();
	}

	~OrderBuilderManager() = default;
private:
	OrderBuilder* order_builder; 
};

//client code which will only interact with the OrderBuilderManager
int main()
{
	OrderBuilderManager obm;
	NativeOrderBuilder nob;
	obm.SetOrderBuilder(&nob);

	NativeOrder* order = obm.GetAndCreateOrder(10, 20.0, 123, "CME");

	order->ShowOrderParams();

	delete order;

	return 0;
