package model;

import io.spring.guides.gs_producing_web_service.Country;
import io.spring.guides.gs_producing_web_service.Currency;
import org.springframework.stereotype.Component;

import javax.annotation.PostConstruct;
import java.util.ArrayList;
import java.util.List;

/**
 * Created by Marcin on 2015-03-11.
 */
@Component
public class CountryRepository {

    private static final List<Country> countries = new ArrayList<Country>();

    @PostConstruct
    public void initData() {
        Country spain = new Country();
        spain.setName("Spain");
        spain.setName("Madrid");
        spain.setCurrency(Currency.EUR);
        spain.setPopulation(4680000);
        countries.add(spain);

        Country poland = new Country();
        poland.setName("Poland");
        poland.setName("warsaw");
        poland.setCurrency(Currency.PLN);
        poland.setPopulation(3880000);
        countries.add(poland);
    }

    public Country findCountry(String name) {
        for(Country c : countries)
            if(c.getName().equals(name))
                return c;

        return null;
    }

}
