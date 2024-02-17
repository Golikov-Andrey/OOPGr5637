package Interfaces;

import java.util.List;

import Classes.Actor;

public interface iMarcketBehaviour {
    public void acceptToMarket(iActorBehaviour actor);
    public void releseFromMarket(List<Actor> actors);
    public void update();
}
