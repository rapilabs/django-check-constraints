from django.db import models


#class CombinedExpressionFacade(models.CombinedExpression):
#    pg_operator_map = {
#        '==': '=',
#        '!=': '<>',
#    }
#
#    def __init__(self, wrapped):
#        self.wrapped = wrapped
#
#    def as_sql(self, compiler, connection):
#        # return super().as_sql(compiler, connection)
#        return 'xxxx'
#
#    def __getattr__(self, name):
#        return getattr(self.wrapped, name)()



class G(models.F):
    output_field = None
    EQ = '='
    NE = '<>'
    LT = '<'
    LE = '<='
    GT = '>'
    GE = '>='

    def __eq__(self, other):
        # return CombinedExpressionFacade(self._combine(other, self.EQ, False))
        return self._combine(other, self.EQ, False)

    def __ne__(self, other):
        # return CombinedExpressionFacade(self._combine(other, self.NE, False))
        return self._combine(other, self.NE, False)

    def as_sql(self, *args):
        return (self.name, [])




# class Sample(models.Model):
#    value_a = models.IntegerField()
#    value_b = models.IntegerField()
#
#    class Meta:
#        check_constraints = (
#            G('value_a') == G('value_b')
#        )
