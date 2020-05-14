class Package:

	def __init__(self):
		pass


	def __init__(self,packageId,address,city,state,zipCode,deadline,weight,notes):
			self._packageId=packageId
			self._address=address
			self._state=state
			self._deadline=deadline
			self._city=city
			self._zipCode=zipCode
			self._weight=weight
			self._notes=notes
			self._deliveryStatus=False
	@classmethod
	def fromAddress(self, add):
			self._packageId=None
			self._address=add
			self._state=None
			self._deadline=None
			self._city=None
			self._zipCode=None
			self._weight=None
			self._notes=None
			self._deliveryStatus=False