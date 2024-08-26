> def pageRank (M, n):
>
> > r_new = r_prev = 1/n \* [1<sub>n</sub>]<sup>T</sup>
> >
> > while (true): #Infinte loop
> >
> > > r_new = M \* r_prev;
> > >
> > > If (r_new ≈ r_prev)
> > >
> > > > break
> > >
> > > r_prev = r_new
> >
> > return r_new
