#include "UPReference.h"
#include "QtGui.h"

UPReference::UPReference(QWidget *parent)
	: QDialog(parent)
{
	
	ui.setupUi(this);
	setWindowTitle(QString::fromLocal8Bit("���������� ��"));
	connect(ui.pb_ExitUP, SIGNAL(clicked()), this, SLOT(exitUPReference()));
}

UPReference::~UPReference()
{
}

void UPReference::exitUPReference()
{
	QtGui* w = new QtGui;
	w->show();
	this->hide();
}